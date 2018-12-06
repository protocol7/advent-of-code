use std::io::{BufRead, BufReader};
use std::fs::File;
use std::collections::HashSet;
use std::iter::FromIterator;

fn valid_vec(ss: Vec<String>) -> bool {
    let ss_len = ss.len();
    let set: HashSet<String> = HashSet::from_iter(ss);
    ss_len == set.len()
}

fn valid(s: &str) -> bool {
    valid_vec(s.split_whitespace().map(|s| s.to_owned()).collect())
}

fn sort_str(s: &str) -> String {
    let mut cs: Vec<char> = s.chars().collect();
    cs.sort();
    cs.iter().collect()
}

fn valid_anagram(s: &str) -> bool {
    valid_vec(s.split_whitespace().map(|s| sort_str(s)).collect())
}

fn main() {
    let file = BufReader::new(File::open("phrases.txt").unwrap());
    let phrases: Vec<_> = file.lines().map(|line| { line.unwrap() }).collect();

    println!("{}", phrases.iter().filter(|p| valid(p)).count());
    println!("{}", phrases.iter().filter(|p| valid_anagram(p)).count());

}

#[test]
fn test_valid() {
    assert!(valid("aa bb"));
    assert!(!valid("aa bb aa"));
}

#[test]
fn test_valid_anagram() {
    assert!(valid_anagram("aa bb"));
    assert!(!valid_anagram("ab ba"));
}
