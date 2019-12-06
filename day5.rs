use std::io;

fn main() {    
    let mut input = String::new();
    let mut inputInt = 0;
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    
    let inputString = input.trim();
    match inputString.parse::<u32>(){
        Ok(i) => inputInt = i,
        Err(..) => println!("this was not an integer: {}", inputString),
        };
    
    for _i in 1..11 {
        println!("{} x {} = {}", inputInt, _i, _i*inputInt)
    }
}
