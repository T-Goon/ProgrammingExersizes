import java.util.*;

public class Queue<T>{
  private final T _array[];
  private int _front;
  private int _back;

  /**
    * @param capacity the capacity of the queue
    */
  public Queue(int capacity){
    this._array = (T[])new Object[capacity];
    this._front = 0;
    this._back = 0;
  }

  /**
    * Adds an item to the queue
    * @param item the capacity of the queue
    * @return true if item was added to the queue and false otherwise
    */
  public boolean enqueue(T item){
    final int nextIndex = (this._front + 1) % this._array.length;
    if(this._front == -1){
    // the queue is full
      return false;
    }
    else{
    this._front = nextIndex;
    this._array[this._front] = item;
    if(this._front == this._back)
      this._front = -1;

    return true;
    }
  }

  /**
    * removes an item from the queue
    * @return the item that was dequeued
    */
  public T dequeue () throws NoSuchElementException{
    final int nextIndex = (this._back + 1) % this._array.length;
    if(this._back == this._front){
    // the queue is empty
      throw new NoSuchElementException();
    }
    else{
    if(this._front ==  -1)
      this._front = this._back;
    this._back = nextIndex;
    return this._array[this._back];
    }
  }

}
