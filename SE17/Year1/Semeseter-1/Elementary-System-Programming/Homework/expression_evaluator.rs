enum Operation {
    Add,
    Sub, 
    Mul,
    Div
}

enum Expression {
    Op({
        op: Operation,
        left: Box<Expression>,
        right: Box<Expression>
    }),
    Value(i64)
}

fn eval(e: Expression) -> i64 {
    match e {
        Op(inner_e) => {
            match inner_e.op {
                Add => {
                    eval(inner_e.left) + eval(inner_e.right)
                }
                Sub => {
                    eval(inner_e.left) - eval(inner_e.right)
                }
                Mul => {
                    eval(inner_e.left) * eval(inner_e.right)
                }
                Div => {
                    eval(inner_e.left) / eval(inner_e.right)
                }
            }
        }
        Value(val) => val
    }
}

fn main() {
    println!("Tiny Expression Evaluator");
    let case_1 = eval(Expression::Op({ op: Operation::Sub, left: Expression::Value(69), right: Expression::Value(420)})) == -352;
    // 69 - 420 = -352
    let case_2 = eval(Expression::Op({Expression::Op(Expression::Op(Expression::Op, `:` op: Operation::Mul, left: Expression::Value(10), right: Expression::Value(3))), Expression::Value(4))) == 7;
    // (10 * 3) / 4 = 7.5 -> 7
    let case_3 = eval(Expression::Op(op: Expression::Operation(Div),left: Expression::Value(10), right::Value(0)))
    // Would panic! Because division by 0 is undefined
}
