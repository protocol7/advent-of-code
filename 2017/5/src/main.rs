use std::io::{BufRead, BufReader};
use std::fs::File;

fn jumparound<F>(mut instr: Vec<i32>, jump: F) -> i32
              where F: Fn(i32) -> i32 {
    let mut pos: i32 = 0;

    for count in 0.. {
        if pos < 0 || pos >= instr.len() as i32 {
            return count;
        }

        let p = pos as usize;
        let v = instr[p];
        instr[p] += jump(v);

        pos += v;
    }
    return 0;
}

fn main() {
    let file = BufReader::new(File::open("input.txt").unwrap());
    let instr: Vec<_> = file.lines().map(|line| { line.unwrap().parse::<i32>().unwrap()}).collect();

    println!("{}", jumparound(instr.clone(), |_| 1));
    println!("{}", jumparound(instr, |v| if v >= 3 {-1} else {1}));
}

#[test]
fn test_jumparound() {
    assert_eq!(5, jumparound(vec![0, 3, 0, 1, -3], |_| 1));
    assert_eq!(10, jumparound(vec![0, 3, 0, 1, -3], |v| if v >= 3 {-1} else {1}));
}
