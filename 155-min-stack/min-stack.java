class MinStack {
    private Stack<Long> s;
    private long min;
    public MinStack() {
        s= new Stack<>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        long value = val;
        if(s.isEmpty()){
            min = value;
            s.push(value);
        }else{
            if(val < min){
                s.push(2*value-min);
                min = value;
            }else{
                s.push(value);
            }
        }
    }
    
    public void pop() {
       if(s.isEmpty())return;
       long el = s.pop();
        if(el < min){
            min =2*min-el;
        }
    }
    
    public int top() {
        if(s.isEmpty())return -1;
        long el = s.peek();
        if(el < min)return (int)min;
        return (int)el;
    }
    
    public int getMin() {
        return (int)min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */