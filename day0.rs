use std::io::{self, Read};

fn get_std_in() -> String {
    let mut buffer = String::new();
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    handle.read_to_string(&mut buffer);
    return buffer
}



fn main() {
    println!("Hello, World. ");
    println!("{}", get_std_in());
}
