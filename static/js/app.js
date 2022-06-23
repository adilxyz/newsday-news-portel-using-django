
document.getElementById("menu-icon").addEventListener("click", () => {
    document.querySelector("#mobile-menu").classList.add("active")
    document.querySelector("span.close").classList.add("active")
    document.querySelector("span.overlay").classList.add("active")
})

document.querySelector("span.close").addEventListener("click", () => {
    document.querySelector("#mobile-menu").classList.toggle("active")
    document.querySelector("span.close").classList.toggle("active")
    document.querySelector("span.overlay").classList.toggle("active")
})

document.querySelector("span.overlay").addEventListener("click", () => {
    document.querySelector("#mobile-menu").classList.toggle("active")
    document.querySelector("span.close").classList.toggle("active")
    document.querySelector("span.overlay").classList.toggle("active")
})

document.querySelector("ul.menu").addEventListener("click", () => {
    document.querySelector("#mobile-menu").classList.toggle("active")
    document.querySelector("span.close").classList.toggle("active")
    document.querySelector("span.overlay").classList.toggle("active")
})