namespace py example

struct Data {
    1: string text
    2: i32 id               
}

service format_data {
    Data do_format(1:Data data),         
}
