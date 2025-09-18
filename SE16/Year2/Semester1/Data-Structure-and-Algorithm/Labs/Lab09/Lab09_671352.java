package Lab09;

import java.nio.channels.Pipe.SourceChannel;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

import Lab09.pack.*;

public class Lab09_671352 {
    static ArrayList<Integer> least3;
    public static void main(String[] args) {
        System.out.println("-task1---");
        task_1();
        System.out.println("-task2---");
        task_2();
        System.out.println("-task3---");
        task_3();
        System.out.println("-task4---");
        task_4();
    }    
    static void task_1() {
        least3 = new ArrayList<>();
        MyMinHeap_671352 heap = new MyMinHeap_671352();
        heap.insert(11);
        heap.insert(15);
        heap.insert(16);
        heap.insert(13);
        heap.insert(17);
        heap.insert(18);
        System.out.println("heap structure is " + heap);
        least3.add(heap.remove()); 
        least3.add(heap.remove()); 
        least3.add(heap.remove()); 
        System.out.println("least 3 value is " + least3);
    } 
    static void task_2() {
        least3 = new ArrayList<>();
        MyPriorityQueue_671352 pq = new MyPriorityQueue_671352();
        pq.enqueue(11);
        pq.enqueue(15);
        pq.enqueue(16);
        pq.enqueue(13);
        pq.enqueue(17);
        pq.enqueue(18);
        pq.enqueue(19); // isFull() is true ...discard
        System.out.println("pq structure is " + pq);
        least3.add(pq.dequeue());;
        least3.add(pq.dequeue());
        least3.add(pq.dequeue());
        System.out.println("least 3 value is " + least3);
    }
    static void task_3() {
        PriorityQueue<Employee> pq = new PriorityQueue<>(
            /* your code */
            (e1, e2) -> Integer.compare(e1.getSalary(), e2.getSalary())
        );
        List<Employee> list = Arrays.asList(new Employee("Yindee", 2000),
                                            new Employee("Preeda", 1500),
                                            new Employee("Pramote", 3000));
        pq.addAll(list);
        System.out.println(pq);
        // [Emp Preeda(1500), Emp Yindee(2000), Emp Pramote(3000)]
    }
    static void task_4() {
        int lastStoneWeight = 0;
        int[] stones = {2,7,4,1,8,1};
        /* your code */

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) pq.add(s);

        while (pq.size() > 1) {
            int y = pq.poll();
            int x = pq.poll();
            if (y > x) pq.add(y - x);
        }
        lastStoneWeight = pq.isEmpty() ? 0 : pq.poll();
        System.out.println(lastStoneWeight);
    }
}
