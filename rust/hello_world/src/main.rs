use raylib::prelude::*;

fn main() {
    println!("Hello, world!");
    let (mut rl, thread) = raylib::init()
        .size(640, 480)
        .title("Hello World!")
        .build();
     
    while !rl.window_should_close() {
        let mut d = rl.begin_drawing(&thread);
         
        d.clear_background(Color::WHITE);
        d.draw_text("Hello, world!", 270, 220, 20, Color::BLACK);
    }
}
