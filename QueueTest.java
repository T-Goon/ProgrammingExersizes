import static org.junit.Assert.*;
import org.junit.Test;
import java.util.*;

public class QueueTest{
  final Queue<Integer> queue = new Queue<Integer>(5);

  @Test
  public void testNormalOperation(){
    assertEquals(true, queue.enqueue(1));
    assertEquals(true, queue.enqueue(null));
    assertEquals((long)1, (long)queue.dequeue());
    assertEquals(null, queue.dequeue());
  }

  @Test
  public void testQueueIsFull(){
    queue.enqueue(1);
    queue.enqueue(null);
    queue.dequeue();
    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);
    assertEquals(true, queue.enqueue(6)); // Full now
    assertEquals(false, queue.enqueue(7));
    assertEquals(false, queue.enqueue(8));
    queue.dequeue();
    assertEquals(true, queue.enqueue(9));
    assertEquals(false, queue.enqueue(10));
  }

  @Test(expected=NoSuchElementException.class)
  public void testQueueIsEmpty(){
    queue.enqueue(null);
    queue.enqueue(null);
    queue.dequeue();
    queue.dequeue();
    queue.dequeue();
  }
}
