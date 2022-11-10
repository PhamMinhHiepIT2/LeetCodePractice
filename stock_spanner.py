
class StockSpanner:
    def __init__(self):
        self.st = []
        self.spans = []


    def next(self, price: int) -> int:
        if not price or not str(price).isdigit():
            # self.span.append(None)
            return None
        if len(self.st) == 0:
            self.st.append(price)
            self.spans.append(1)
            return 1
        else:
            span = find_seq(self.st, price, self.spans)
            self.st.append(price)
            self.spans.append(span)
            return span 
    def print_res(self):
        print(f"ST: {self.st}")
        print(f"Spans: {self.spans}")

        
def find_seq(arr: list, target: int, span: list):
    n = len(arr)
    print(f"arr: {arr} | target: {target} | spans: {span}")
    c = n-1
    res = 1
    while target >= arr[c] and c >= 0:
        res += span[c]
        c -= span[c]
    return res

if __name__ == "__main__":
    a = StockSpanner()
    a.next(100)
    a.next(80)
    a.next(90)
    a.next(95)
    a.next(70)
    a.print_res()
