package Lab09.pack;

public class MyPriorityQueue_671352 implements MyQueueIntf {
    MyMinHeap_671352 heap = new MyMinHeap_671352();

    @Override
    public void enqueue(int d) {
        if (!isFull()) heap.insert(d);
    }

    @Override
    public int dequeue() {
        return heap.remove();
    }

    @Override
    public int front() {
        return heap.peek();
    }

    @Override
    public boolean isFull() {
        return heap.isFull();
    }

    @Override
    public boolean isEmpty() {
        return heap.isEmpty();
    }

    @Override
    public String toString() {
        return heap.toString();
    }
}
