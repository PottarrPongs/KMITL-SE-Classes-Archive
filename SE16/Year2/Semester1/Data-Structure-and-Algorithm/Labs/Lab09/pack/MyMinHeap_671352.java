package Lab09.pack;

public class MyMinHeap_671352 {
    int MAX_SIZE = 100;
    int heap[] = new int[MAX_SIZE];
    int size = 0;

    private void swap(int i, int j) {
        heap[i] = heap[i] + heap[j];
        heap[j] = heap[i] - heap[j];
        heap[i] = heap[i] - heap[j];
    }
    public int peek() {
        return heap[0];
    }

    public boolean isFull() {
        return size == MAX_SIZE;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void insert(int d) {
        /* your code */
        if (isFull()) return;
        heap[size] = d;
        int i = size;
        size++;

        while (i > 0) {
            int parent = (i - 1) / 2;
            if (heap[i] < heap[parent]) {
                swap(i, parent);
                i = parent;
            } else break;
        }
    }

    public int remove() {
        int d = heap[0];
        heap[0] = heap[--size];
        heap[size] = d;
        int p = 0;
        while (true) {
            /* your code */
            int left = 2 * p + 1;
            int right = 2 * p + 2;
            int smallest = p;

            if (left < size && heap[left] < heap[smallest]) smallest = left;
            if (right < size && heap[right] < heap[smallest]) smallest = right;

            if (smallest != p) {
                swap(p, smallest);
                p = smallest;
            } else break;

            System.out.println("heap snapshot (cur_size = " + size + ") " + this.toString());
        }
        return d;
    } //end while

    public String toString() {
        int i;
        StringBuffer sb = new StringBuffer();
        sb.append("[");
        for (i = 0; i < size; i++) {
            sb.append(heap[i]);
            sb.append(",");
        }
        if (size > 0) {
            sb.append("]");
        }
        return sb.toString();
    }

}
