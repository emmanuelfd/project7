
// to clear the page when reload
document.getElementById("dialogue").value = ""
document.getElementById("msg").value = ""

var dialogues = []
//intro from GrandPy
var grandpy = ["Tiens savais-tu que ","A propos il faut que tu saches que ", "Pour ton info, "]



$('#msg').keypress(function(e) {
  if(e.which == 13) {


    $(function () {


        entry_user = document.getElementById("msg").value.replace(/\n/g, "")//remove newline
        entry_user = entry_user.trim()//remove blank if needed
        entry_grandpy = grandpy[Math.floor(Math.random() * 3)]//pick up 1 random intro from grandpy

        $.ajax({
           type : "POST", // Le type de la requête HTTP.
           //url : "http://127.0.0.1:5000/GrandPy", //
            url : "GrandPy", // La ressource ciblée
           data : "msg=" + entry_user,
           dataType : "json",
           success: function(data)
               {

                   reponse = (data["google"]);
                   console.log(reponse);
                   //console.log(entry_user);
                   //remove id=plan to clear any existing map
                   document.getElementById("google").removeChild(document.getElementById("plan"));

                   var img = document.createElement("img");
                   img.id = 'plan'


                   img.src = reponse;
                   var src = document.getElementById("google");
                   src.appendChild(img);

                   ///

                   var wiki_string = (data["wiki"]);

                   //add in the list [dialogues] to be able to retreive previous request

                   dialogues.unshift('\n*-*-*-*\n\n')
                   dialogues.unshift(wiki_string)
                   dialogues.unshift(entry_grandpy)
                   dialogues.unshift(entry_user + "\n")


                   document.getElementById("dialogue").value = ''//clear dialogue as it will be added again

                   //re-add the whole list [dialogues]
                   var i;
                   for (i = 0; i < dialogues.length; ++i) {
                       document.getElementById("dialogue").value += dialogues[i]
                       console.log(dialogues[i]);

                   }


               },
           error: function(request, error)
               {console.log("ERROR")}



        });

    });

  }
});
