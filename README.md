amanda is a tool to strip your java source code to make it naked.
This tool is useful to hide solutions in programming exercises.

A file with input:

    public int computeSum(int a, int b) {
    // STUDENT return 0; // TODO
    // BEGIN STRIP
        return a + b; // the solution to hide
    // END STRIP
    }

Gives as output:

    public int computeSum(int a, int b) {
        return 0; // TODO
    }