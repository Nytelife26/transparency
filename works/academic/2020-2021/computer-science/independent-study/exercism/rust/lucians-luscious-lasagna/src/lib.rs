pub fn expected_minutes_in_oven() -> i32 {
	40
}

pub fn remaining_minutes_in_oven(elapsed_mins: i32) -> i32 {
	expected_minutes_in_oven() - elapsed_mins
}

pub fn preparation_time_in_minutes(num_layers: i32) -> i32 {
	2 * num_layers
}

pub fn elapsed_time_in_minutes(num_layers: i32, elapsed_mins: i32) -> i32 {
	elapsed_mins + preparation_time_in_minutes(num_layers)
}
