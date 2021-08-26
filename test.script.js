console.log("Testing page.");
$(".messages").css({"height":$(".messages").height()-50});

function send_message() {
  var currentdate = new Date();
  var textarea = document.getElementById('message-to-send').value;
  const mediv = document.createElement("div");
  mediv.classList.add("me");
  const inf = document.createElement('p');
  inf.classList.add("inf");
  const infnode = document.createTextNode(textarea);
  inf.appendChild(infnode);
  mediv.appendChild(inf);
  const time = document.createElement('p');
  time.classList.add("time");
  const timenode = document.createTextNode("Me, " + String(currentdate).split("G")[0]);
  time.appendChild(timenode);
  mediv.appendChild(time);
  const element = document.getElementById("messages-add");
  element.appendChild(mediv);
  var objDiv = document.getElementById("messages-add");
  objDiv.scrollTop = objDiv.scrollHeight;
}


//Starred svg for placement of contacts
//<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
//<path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
//</svg>
