src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"

$(document).ready(function() {
    let BASE_URL = "https://api.coingecko.com/api/v3/coins/";
    let COINS_ENDPOINT = "";

    let pageSize = 100;
    let curPageNum = 0;

  populateTable();

  function getData(){
    ENDPOINT = "markets?vs_currency=usd&order=market_cap_desc&per_page=${pageSize}&page=${curPageNum}&sparkline=true&Price_change_percentage=1h%2C%2024h%2C%207d%2C%2014d%2C%2030d%2C%20200d%2C%201y";
    let url = BASE_URL + ENDPOINT;
    return fetch(url)
    .then(function (response) {
        return response.json();
    }).catch(function (error) {
        console.log(error);
    });
  }

  async function populateTable () {
    let coin = await getData();
    const coinTable = $('#coinTable');
    for(let i=0;i<pageSize;i++){
      var img = new Image(20, 20)
      img = document.createElement('img');
      img.src = (coin[i].image.replace("large","thumb"));
      console.log (coin[i].image)
      coinTable.append(
        $('<tr class="content-row"></tr>').append(
          $('<td class="text-left"></td>').text(i+1),
          $('<td class="text-left"></td>').html(img),
          $('<td class="text-left"></td>').text(coin[i].name),
          $('<td class="text-left"></td>').text(coin[i].symbol),
          $('<td class="text-left"></td>').text((coin[i].current_price).toFixed(2) + " " + "$"),
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_1h_in_currency) + " %"),  
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_24h_in_currency) + " %"),
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_7d_in_currency) + " %"),
          $('<td class="text-left"></td>').text((coin[i].total_volume).toFixed(2) + "$US"),
          $('<td class="text-left"></td>').text(coin[i].market_cap),
          $('<td class="text-left"></td>').text(coin[i].sparkline_in_7d),
        )
  
      )
      
    }
  }

  document.querySelector('button').addEventListener('click', fav);
    
  function fav(e) {
    const tgt = e.target.firstElementChild;
    tgt.classList.toggle('fa-star');
    tgt.classList.toggle('fa-star-o');
  }
});