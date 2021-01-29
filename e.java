import java.lang.reflect.Array;
import java.lang.reflect.Method;

import jdk.javadoc.internal.doclets.toolkit.builders.MethodBuilder;

class e {
    
    // Create Variables
    int[] egg = {1,2,3};
    int[] anotherEgg = {4,5,6};

    public static void main(String[] args) {
        
        System.out.println("SCIENCE OOH!");

    }

    void eee() {

        // Print egg to console
        System.out.println(egg);

        // math?
        egg = anotherEgg;

        // Print egg to console again
        System.out.println(egg);

    }

}