const startDate = document.querySelector("#startDate")
const endDate = document.querySelector("#endDate")

// startDate.addEventListener("change", (event) => {
//     endDate.min = startDate.value + 1;
// });
// endDate.addEventListener("change", (event) => {
//     startDate.max = endDate.value - 1;
// });

function test() {
    endDate.min = startDate.value + 1;
    startDate.max = endDate.value - 1;
}