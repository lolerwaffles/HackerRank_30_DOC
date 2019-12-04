use std::io;

fn main() {    
    let mut input = String::new();

    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    
    let inputString:i8 = input.parse().unwrap();
    if(inputString % 2 != 0 || (inputString >= 6 && inputString <=20 && inputString % 2 ==0)){
        println!("Weird");
     }else{
         println!("Not Weird");
     }
}
