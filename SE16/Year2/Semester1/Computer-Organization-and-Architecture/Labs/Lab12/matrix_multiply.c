#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define SIZE 500 // Adjustable matrix size
#define BLOCK_SIZE 32 // Cache block size, adjustable for optimization

// Declare the matrices
int (*matrixA)[SIZE];
int (*matrixB)[SIZE];
int (*result)[SIZE];

typedef struct {
    int thread_id;
    int start_row;
    int end_row;
} thread_data_t;

// Optimized multiply function with cache blocking
void *multiply(void *arg) {
    thread_data_t *data = (thread_data_t *)arg;
    int start_row = data->start_row;
    int end_row = data->end_row;
    
    for (int i = start_row; i < end_row; i += BLOCK_SIZE) {
        for (int j = 0; j < SIZE; j += BLOCK_SIZE) {
            for (int k = 0; k < SIZE; k += BLOCK_SIZE) {
                // Block multiplication
                for (int ii = i; ii < i + BLOCK_SIZE && ii < end_row; ii++) {
                    for (int jj = j; jj < j + BLOCK_SIZE && jj < SIZE; jj++) {
                        int sum = result[ii][jj];
                        for (int kk = k; kk < k + BLOCK_SIZE && kk < SIZE; kk++) {
                            sum += matrixA[ii][kk] * matrixB[kk][jj];
                        }
                        result[ii][jj] = sum;
                    }
                }
            }
        }
    }
    pthread_exit(NULL);
}

// Function to initialize matrix with random values
void initialize_matrix(int (*matrix)[SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            matrix[i][j] = rand() % 10; // Random values 0-9
        }
    }
}

// Function to validate results (for testing purposes)
void validate_result(int (*matrixA)[SIZE], int (*matrixB)[SIZE], int (*result)[SIZE]) {
    int *expected_result = malloc(SIZE * SIZE * sizeof(int));
    if (expected_result == NULL) {
        fprintf(stderr, "Memory allocation failed for validation.\n");
        return;
    }

    // Compute expected result
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            expected_result[i * SIZE + j] = 0;
            for (int k = 0; k < SIZE; k++) {
                expected_result[i * SIZE + j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }

    // Compare with actual result
    int errors = 0;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (result[i][j] != expected_result[i * SIZE + j]) {
                errors++;
            }
        }
    }

    if (errors == 0) {
        printf("Validation successful. All elements match.\n");
    } else {
        printf("Validation failed. %d elements do not match.\n", errors);
    }

    free(expected_result);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <number_of_threads>\n", argv[0]);
        return 1;
    }
    int num_threads = atoi(argv[1]);
    if (num_threads <= 0 || num_threads > SIZE) {
        printf("Invalid number of threads. Please choose between 1 and %d.\n", SIZE);
        return 1;
    }

    // Allocate memory for matrices
    matrixA = malloc(SIZE * sizeof(*matrixA));
    matrixB = malloc(SIZE * sizeof(*matrixB));
    result = malloc(SIZE * sizeof(*result));
    if (!matrixA || !matrixB || !result) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Initialize matrices
    srand(time(NULL));
    initialize_matrix(matrixA);
    initialize_matrix(matrixB);

    // Initialize result matrix to 0
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            result[i][j] = 0;
        }
    }

    pthread_t threads[num_threads];
    thread_data_t thread_data[num_threads];

    int rows_per_thread = SIZE / num_threads;
    int remaining_rows = SIZE % num_threads;

    clock_t start = clock();

    // Create threads
    for (int i = 0; i < num_threads; i++) {
        thread_data[i].thread_id = i;
        thread_data[i].start_row = i * rows_per_thread + (i < remaining_rows ? i : remaining_rows);
        thread_data[i].end_row = (i + 1) * rows_per_thread + (i < remaining_rows ? i + 1 : remaining_rows);
        pthread_create(&threads[i], NULL, multiply, (void *)&thread_data[i]);
    }

    // Join threads
    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    clock_t end = clock();
    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Matrix size: %dx%d\n", SIZE, SIZE);
    printf("Block size: %d\n", BLOCK_SIZE);
    printf("Number of threads: %d\n", num_threads);
    printf("Execution time: %.2f seconds\n", time_taken);

    // Uncomment the following line to validate results (warning: slow for large matrices)
    // validate_result(matrixA, matrixB, result);

    // Free allocated memory
    free(matrixA);
    free(matrixB);
    free(result);

    return 0;
}
