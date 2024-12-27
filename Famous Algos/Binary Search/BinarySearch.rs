fn binary_search(array: &[i32], target_number: i32) -> bool {
    let mut start_pointer = 0;
    let mut end_pointer = array.len() - 1;
    let mut found = false;

    while start_pointer <= end_pointer {
        let mid_pointer = (start_pointer + end_pointer) / 2;
        if array[mid_pointer] == target_number {
            found = true;
            break;
        }
        else if array[mid_pointer] > target_number {
            end_pointer = mid_pointer - 1;
        } else {
            start_pointer = mid_pointer + 1;
        }
    }

    return found;
}

fn main() {
    let result = binary_search(&[1, 2, 3, 4, 5, 6, 7], 1);
    println!("{}", result)
}
