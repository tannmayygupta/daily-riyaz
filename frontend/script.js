async function saveEntry() {

    const content =
        document.getElementById("entry").value;

    const status =
        document.getElementById("status");

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/entry",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    content: content
                })
            }
        );

        const data = await response.json();

        status.innerText =
            data.message;

    } catch (error) {

        status.innerText =
            "Something went wrong";
    }
}