use std::io::{BufRead, BufReader};
use std::fs::File;
use std::i32;
use std::cmp::{min, max};

fn split_row(s: &String) -> Vec<i32> {
    s.split_whitespace().map(|i| i.parse::<i32>().unwrap()).collect::<Vec<i32>>()
}

fn min_max(xs: &Vec<i32>) -> (i32, i32) {
    xs.iter().fold((i32::MAX, i32::MIN), |(mi, ma), x| (min(mi, *x), max(ma, *x)))
}

fn chk(rows: &Vec<Vec<i32>>) -> i32 {
    rows.iter().map(|row| min_max(row)).map(|(min, max)| max - min).sum::<i32>()
}

fn div_sum(x: i32, ys: &Vec<i32>) -> i32 {
    // a bit of a hack, as we're looking for sums, just mapping to 0 if not divisible ¯\_(ツ)_/¯
    ys.iter().map(|y| if x != *y && x % y == 0 {x/y} else {0}).sum::<i32>()
}

fn div_sums(xs: &Vec<i32>) -> i32 {
    xs.iter().map(|x| div_sum(*x, xs)).sum()
}

fn divisble_sum(rows: &Vec<Vec<i32>>) -> i32 {
    rows.iter().map(|row| div_sums(row)).sum::<i32>()
}

fn main() {
    let file = BufReader::new(File::open("sheet.txt").unwrap());
    let lines: Vec<_> = file.lines().map(|line| { line.unwrap() }).collect();
    let rows: Vec<Vec<i32>> = lines.iter().map(|line| split_row(line)).collect::<Vec<Vec<i32>>>();

    println!("{}", chk(&rows));
    println!("{}", divisble_sum(&rows));
}
