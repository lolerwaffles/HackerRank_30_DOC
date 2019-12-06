use std::io;

fn main(){
    let mut wordList = Vec::new();
    for _i in 0..readSTDinINT(){
        wordList.push(readSTDinString())
    }
    
    for _word in wordList.iter(){
        for (i,_letter) in _word.chars().enumerate(){
            if i % 2 == 0{
                print!("{}", _letter)
            }
        }
        print!(" ");
        for (i,_letter) in _word.chars().enumerate(){
            if i % 2 != 0{
                print!("{}", _letter)
            }
        }
        print!("\n")
    }
}

fn readSTDinINT() -> i8{
    let mut input = String::new();
    let mut inputInt = 0;

    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    
    let inputString = input.trim();
    match inputString.parse::<i8>() {
        Ok(i) => inputInt = i,
        Err(..) => println!("this was not an integer: {}", inputString),
        };
    (inputInt)
}

fn readSTDinString() -> String{
    let mut input = String::new();
    let mut outputString = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");
    
    let inputString = input.trim();
    match inputString.parse::<String>() {
        Ok(i) => outputString = i,
        Err(..) => println!("this was not a String: {}", inputString),
        };
    (outputString)
}
