use std::collections::HashMap;

// rustc -O fun.rs

fn fun(a: u16, b: u16, c: u16, cache: &mut HashMap<(u16, u16), u16>) -> u16 {
    if let Some(x) = cache.get(&(a, b)) {
        return *x;
    }

    let x = if a == 0 {
        b + 1
    } else {
        if b == 0 {
            fun(a - 1, c, c, cache)
        } else {
            let x = fun(a, b - 1, c, cache);
            fun(a - 1, x, c, cache)
        }
    };

    cache.insert((a, b), x);
    return x;
}

fn main() {
    for c in 1..32767 {
        let mut cache: HashMap<(u16, u16), u16> = HashMap::new();

        let x = fun(4, 1, c, &mut cache);
        println!("{}, {}", c, x);

        if x == 6 {
            break;
        }
    }

}