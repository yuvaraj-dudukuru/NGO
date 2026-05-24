let password = document.getElementById("password");
let power = document.getElementById("power-point");

password.oninput = function() {
    let point = 0;
    let value = password.value;
    let widthpower = ["0%", "25%", "50%", "75%", "100%"];
    let color = ["red", "orange", "yellow", "lightgreen", "green"];

    if (value.length >= 6){
        let arrayTest = [/[a-z]/, /[A-Z]/, /[0-9]/, /[^a-zA-Z0-9]/];
        arrayTest.forEach((item) => {
            if (item.test(value)){
                point += 1;
            }
        });
    }
    power.style.width = widthpower[point];
    power.style.backgroundColor = color[point];
}


