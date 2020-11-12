import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class LCA1test {

	
	@Test
	void test() {
		
		LCA1 tree = new LCA1(); 
        tree.root = new Node(1); 
        tree.root.left = new Node(2); 
        tree.root.right = new Node(3); 
        tree.root.left.left = new Node(4); 
        tree.root.left.right = new Node(5); 
        tree.root.right.left = new Node(6); 
        tree.root.right.right = new Node(7);
        
		
		assertEquals(2, tree.findLCA(4,5));
		assertEquals(1, tree.findLCA(4,6));
		assertEquals(1, tree.findLCA(3,4));
		assertEquals(2, tree.findLCA(2,4));
		
	}
	@Test
	void testInvalid() {
		
		LCA1 tree = new LCA1(); 
        tree.root = new Node(1); 
        tree.root.left = new Node(2); 
        tree.root.right = new Node(3); 
        tree.root.left.left = new Node(4); 
        tree.root.left.right = new Node(5); 
        tree.root.right.left = new Node(6); 
        tree.root.right.right = new Node(7);
        
        assertEquals(-1, tree.findLCA(8, 9));
	}
	@Test
	void testEmpty() {
		
		LCA1 tree = new LCA1();
		tree.root = null;
		
		assertEquals(-1, tree.findLCA(2, 1));
	}

}
