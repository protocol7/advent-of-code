use std::collections::HashMap;

fn get_coord(cell: i32) -> (i32, i32) {
    // TOOO this is ugly (but dies the job)

    let xx = ((cell as f64).sqrt().ceil()) as i32;
    let layer = if xx % 2 == 1 {xx} else {xx+1};
    let y = (layer - 1) / 2;
    let lower_right = layer * layer;

    // calculate values at main directions
    let bottom = lower_right - y;
    let left = lower_right - (layer - 1) - y;
    let top = lower_right - 2 * (layer - 1) - y;
    let right = lower_right - 3 * (layer - 1) - y;

    if cell >= lower_right - (layer - 1) {
        (cell - bottom, -y)
    } else if cell >= lower_right - 2*(layer-1) {
        (-y, left - cell)
    } else if cell >= lower_right - 3*(layer-1) {
        (top - cell, y)
    } else {
        (y, cell - right)
    }
}

fn distance(cell: i32) -> i32 {
    let (x, y) = get_coord(cell);
    x.abs() + y.abs()
}

const SURROUND: [(i32, i32); 8] = [(-1,-1), (0,-1),(1,-1),
                                   (-1,0), (1,0),
                                   (-1,1), (0,1),(1,1)];

fn fill_up_to(threshold_value: i32) -> i32 {
    let mut cache = HashMap::new();
    // first cell is special case, add here
    cache.insert((0,0), 1);

    for cell in 2.. {
        let (x, y) = get_coord(cell);

        let sum = SURROUND.iter().map(|&(sx, sy)| cache.get(&(x+sx, y+sy)).unwrap_or(&0)).sum::<i32>();

        if sum > threshold_value {
            return sum;
        }

        cache.insert((x, y), sum);
    }
    return 0;
}

fn main() {
    let cell = 368078;

    println!("{}", distance(cell));
    println!("{}", fill_up_to(cell));
}

#[test]
fn test_get_coord() {
    assert_eq!((1, 0), get_coord(2));
    assert_eq!((2, 2), get_coord(13));
    assert_eq!((-2, 2), get_coord(17));
    assert_eq!((-2, -2), get_coord(21));
    assert_eq!((0, -2), get_coord(23));
    assert_eq!((2, -2), get_coord(25));
    assert_eq!((0, 0), get_coord(1));
}

#[test]
fn test_distance() {
    assert_eq!(371, distance(368078));
}

#[test]
fn test_fill_up_to() {
    assert_eq!(2, fill_up_to(1));
    assert_eq!(4, fill_up_to(2));
    assert_eq!(5, fill_up_to(4));
    assert_eq!(10, fill_up_to(5));
    assert_eq!(369601, fill_up_to(368078));
}
