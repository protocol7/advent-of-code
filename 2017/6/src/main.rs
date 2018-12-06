use std::i32;
use std::collections::HashMap;

fn balance(mut m: Vec<i32>) -> Vec<i32> {
    // find the max index
    let (mut index, _) = m.iter().enumerate().fold((0, i32::MIN), |(max_i, max_x), (i, x)| if x > &max_x {(i, *x)} else {(max_i, max_x)});

    let c = m[index];
    m[index] = 0;

    for _ in 0..c {
        index += 1;
        if index >= m.len() {
            index = 0;
        }
        m[index] += 1;
    }

    m
}

fn balance_loop(mut memory: Vec<i32>) -> (i32, i32) {
    let mut dups = HashMap::new();
    dups.insert(memory.clone(), 0);

    for count in 1.. {
        memory = balance(memory);

        {
            let x = dups.get(&memory);
            if x.is_some() {
                return (count, count - x.unwrap());
            }
        }

        dups.insert(memory.clone(), count);
    }
    return (0, 0);
}

fn main() {
    let memory = vec![0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11];

    println!("{:?}", balance_loop(memory));
}

#[test]
fn test_balance_loop() {
    assert_eq!((5, 4), balance_loop(vec![0, 2, 7, 0]));
    assert_eq!((7864, 1695), balance_loop(vec![0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]));
}
