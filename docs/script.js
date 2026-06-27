async function sendLink(){

    const link = document.getElementById("meetLink").value;
    const status = document.getElementById("status");

    if(!link.includes("meet.google.com")){
        status.innerHTML = "❌ Invalid Meet Link";
        return;
    }

    try{

        const response = await fetch(
            " https://wired-upon-bootleg.ngrok-free.dev/join",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    link:link
                })
            }
        );

        if(response.ok){
            status.innerHTML = "✅ Link sent successfully";
        }else{
            status.innerHTML = "❌ Server error";
        }

    }catch(err){
        status.innerHTML = "❌ Laptop offline";
    }
}