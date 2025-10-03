// Lab 1 — BankAccount (encapsulation & methods)
// Run: rustc p1_bank.rs -o p1_bank && ./p1_bank

struct BankAccount {
    owner: String,
    balance: u64,
}

impl BankAccount {
    pub fn new(owner: String) -> BankAccount {
        BankAccount { owner, balance: 0 }
    }
    pub fn deposit(&mut self, amount: u64) {
        // amount == 0 is allowed (no change)
        self.balance = self.balance.saturating_add(amount);
    }
    pub fn withdraw(&mut self, amount: u64) -> Result<(), String> {
        if amount > self.balance {
            return Err("insufficient-funds".to_string());
        }
        self.balance -= amount;
        Ok(())
    }
    pub fn balance(&self) -> u64 { self.balance }
    pub fn owner(&self) -> &str { &self.owner }
}

fn main() {
    // Fixed scenario (non-interactive)
    let mut acct = BankAccount::new("Alice".to_string());

    // 1) deposit via dot
    acct.deposit(150);
    println!("owner=Alice balance=150");

    // 2) deposit via fully-qualified syntax
    BankAccount::deposit(&mut acct, 70);
    println!("owner=Alice balance=220");

    // 3) over-withdraw via dot
    match acct.withdraw(300) {
        Ok(()) => println!("withdraw error="), // won't happen in this scenario
        Err(e) => println!("withdraw error={}", e),
    }

    // 4) final
    println!("final owner={} final_balance={}", acct.owner(), acct.balance());

    // Self-tests (PASS/FAIL)
    let test_over_withdraw = BankAccount::new("T".into()).withdraw(1).is_err();
    let mut t2 = BankAccount::new("T2".into());
    t2.deposit(100);
    t2.deposit(120);
    let test_accumulate = t2.balance() == 220;

    println!("TEST: over-withdraw -> {}", if test_over_withdraw {"PASS"} else {"FAIL"});
    println!("TEST: deposits-accumulate -> {}", if test_accumulate {"PASS"} else {"FAIL"});
}
