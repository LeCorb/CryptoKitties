$(document).ready(function() {
  let BASE_URL = "https://api.coingecko.com/api/v3/";
  let COINS_ENDPOINT = "";

  let pageSize = 100;
  let curPageNum = 0;

  populateTable();

  function getData(){
    ENDPOINT = `coins/markets?vs_currency=usd&per_page=${pageSize}&page=${curPageNum}`;
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
      var myImage = new Image(30, 30);
      myImage.src = (coin[i].image).html;

      coinTable.append(
        $('<tr class="content-row"></tr>').append(
          $('<td class="text-left"></td>').text(i+1),
          $('<td class="text-left"></td>').text(coin[i].image),
          $('<td class="text-left"></td>').text(coin[i].name),
          $('<td class="text-left"></td>').text(coin[i].market_cap),
          $('<td class="text-left"></td>').text((coin[i].current_price).toFixed(2) + " " + "$"),
          $('<td class="text-left"></td>').text(coin[i].total_volume),
          $('<td class="text-left"></td>').text(coin[i].circulating_supply),
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_24h).toFixed(2) + "%"),
        )
      )
    }
  }
});
