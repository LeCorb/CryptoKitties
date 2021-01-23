src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js";
src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js";
href='https://cdn.jsdelivr.net/fontawesome/4.7.0/css/font-awesome.min.css';
href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
      integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
      crossorigin="anonymous";
src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
      integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" 
      crossorigin="anonymous";
$(document).ready(function() {
    let BASE_URL = "https://api.coingecko.com/api/v3/coins/";
    let COINS_ENDPOINT = "";

    let pageSize = 200; //not working
    let curPageNum = 0; //how to change page

  populateTable();

  function getData(){
    ENDPOINT = "markets?vs_currency=usd&order=market_cap_desc&per_page=${pageSize}&page=${curPageNum}&sparkline=true&price_change_percentage=1h%2C24h%2C7d";
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
      var img = document.createElement('img');
      img.src = (coin[i].image.replace("large","thumb"));
      console.log ((coin[1].price_change_percentage_1h_in_currency))
      coinTable.append(
        $('<tr class="content-row"></tr>').append(
          $('<td class="text-right"></td>').text(i+1),
          $('<td class="text-center"></td>').html(img),
          $('<td class="text-left"></td>').text(coin[i].name),
          $('<td class="text-center"></td>').text((coin[i].symbol).toUpperCase()),
          $('<td class="text-center"></td>').text(new Intl.NumberFormat('en-EN', { style: 'currency', currency: 'USD' }).format(coin[i].current_price)),
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_1h_in_currency).toPrecision(2) + " %"),
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_24h_in_currency).toPrecision(2) + " %"),
          $('<td class="text-left"></td>').text((coin[i].price_change_percentage_7d_in_currency).toPrecision(2) + " %"),
          $('<td class="text-left"></td>').text(new Intl.NumberFormat('en-EN', { style: 'currency', currency: 'USD' }).format(coin[i].total_volume)),
          $('<td class="text-left"></td>').text(new Intl.NumberFormat('en-EN', { style: 'currency', currency: 'USD' }).format(coin[i].market_cap)),
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