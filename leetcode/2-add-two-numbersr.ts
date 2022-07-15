class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = val || 0;
        this.next = next === undefined ? null : next;
    }
}

function reverseLinkedList (start: ListNode) {
    let out;

    function visit (node) {
        if (!node.next) {
            out = new ListNode(node.val);
            return;
        }

        visit(node.next);

        let end = out;
        while (end.next) {
            end = end.next;
        }
        end.next = new ListNode(node.val);
    }

    visit(start);
    return out;
}

function llToNum (start: ListNode): string {
    let val = '';

    while (start.next) {
        val += start.val.toString();
        start = start.next;
    }

    val += start.val;

    return val;
}

function add (n1: string, n2: string): string {
    if (n1.length < n2.length) {
        let temp = n1;
        n1 = n2;
        n2 = temp;
    }

    for (let i = n2.length; i < n1.length; i++) {
        n2 = '0' + n2;
    }

    let sum = '';
    let carry = 0;
    let diff = n1.length - n2.length;

    for (let i = n1.length - 1; i >= 0; i--) {
        const temp =
            (Number(n1.charAt(i)) % 10) +
            (Number(n2.charAt(i + diff)) % 10) +
            carry;

        if (temp >= 10) {
            sum = (temp % 10) + sum;
            carry = Math.floor(temp / 10);
        } else {
            sum = temp + sum;
            carry = 0;
        }
    }
    if (carry) {
        sum = carry + sum;
    }
    return sum;
}

function addTwoNumbers (l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let n1 = llToNum(reverseLinkedList(l1));
    let n2 = llToNum(reverseLinkedList(l2));
    let n = add(n1, n2);

    let node = new ListNode();
    let root = node;

    for (let i = n.length-1; i >= 0; i--) {
        node.val = parseInt(n[i]);
        if (i !== 0) {
            node.next = new ListNode();
            node = node.next;
        }
    }

    return root;
}

console.log(addTwoNumbers(
    new ListNode(2, new ListNode(4, new ListNode(3))),
    new ListNode(5, new ListNode(6, new ListNode(4)))
));