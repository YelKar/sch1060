

function goto(url, download=false) {
    let linkElement = document.createElement("a")
    if (download) {
        linkElement.download = download;
    }
    linkElement.href = url;
    linkElement.click()
}


async function url_for(func, args) {
    return await (
        await fetch(
            document.getElementById("url_for").value + (func || ""),
            {
                method: "POST",
                body: args != undefined ? JSON.stringify(
                    args
                ) : args
            }
        )
    ).text()
}
