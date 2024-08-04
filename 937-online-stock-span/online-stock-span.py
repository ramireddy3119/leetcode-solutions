class StockSpanner:

    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        st = self.stack
        curr_price,curr_span = price,1
        while st and st[-1][0] <= curr_price:
            prev_price_quote, prev_price_span = st.pop()

            curr_span += prev_price_span
        st.append((curr_price,curr_span))
        return curr_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)