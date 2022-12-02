const btn = document.querySelector("button")
const input = document.querySelector("input")
const result = document.querySelector("div > span")

btn.addEventListener("click",  async ev => {
    let res = await fetch("/post", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            x: input.value
        })
    })
    let text = await res.text()
    console.log(text)
    result.textContent = text
})