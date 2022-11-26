// api url
const api_url = 
      "https://638064bb2f8f56e28ea2489f.mockapi.io/critical_tweets/atlassian";
  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    // if (response) {
    //     hideloader();
    // }
    show(data);
}
// Calling that async function
getapi(api_url);
  
// Function to hide the loader
// function hideloader() {
//     document.getElementById('loading').style.display = 'none';
// }
// Function to define innerHTML for HTML table
function show(data) {
    let tab = 
        `<tr>
          <th>S.No.</th>
          <th>Tweet ID</th>
          <th>Tweet Text</th>
          <th>Tweet Link</th>
         </tr>`;
    
    let cnt=1;
    // Loop to access all rows 
    for (let r of data.list) {
        tab += `<tr> 
    <td>${cnt} </td>
    <td>${r.TweetID}</td>
    <td>${r.TweetText}</td> 
    <td>${r.TweetLink}</td>          
</tr>`;
        cnt = cnt+1;
    }
    // Setting innerHTML as tab variable
    document.getElementById("tableValues").innerHTML = tab;
}