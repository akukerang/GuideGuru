/**
 * 
 */
// Your JSON data\
var restaurants = [
    {
        'name': 'Dolores But You Can Call Me Lolita',
        'address': '1000 S Miami Ave, Miami, FL 33130, United States',
        'location': {'lat': 25.7642717, 'lng': -80.1934058},
        'rating': 4.7,
        'price_level': 2,
        'types': ['restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 5419
    },
    {
        'name': 'Toscana Divino',
        'address': '900 S Miami Ave Space 185, Miami, FL 33130, United States',
        'location': {'lat': 25.7649377, 'lng': -80.1935688},
        'rating': 4.3,
        'price_level': 2,
        'types': ['bar', 'restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 748
    },
    {
        'name': 'LPM Restaurant & Bar',
        'address': '1300 Brickell Bay Dr, Miami, FL 33131, United States',
        'location': {'lat': 25.760372, 'lng': -80.190197},
        'rating': 4.5,
        'price_level': 4,
        'types': ['bar', 'restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 813
    },
    {
        'name': "Truluck's Ocean's Finest Seafood and Crab",
        'address': '777 Brickell Ave suite 110, Miami, FL 33131, United States',
        'location': {'lat': 25.766409, 'lng': -80.189904},
        'rating': 4.6,
        'price_level': 3,
        'types': ['bar', 'meal_takeaway', 'restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 1916
    },
    {
        'name': 'Dirty French Steakhouse Miami',
        'address': '1200 Brickell Ave, Miami, FL 33131, United States',
        'location': {'lat': 25.7619992, 'lng': -80.1923449},
        'rating': 3.9,
        'price_level': 4,
        'types': ['restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 243
    },
    {
        'name': 'Crazy About You',
        'address': '1155 Brickell Bay Dr #101, Miami, FL 33131, United States',
        'location': {'lat': 25.7620008, 'lng': -80.1889886},
        'rating': 4.7,
        'price_level': 2,
        'types': ['restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 8609
    },
    {
        'name': 'The Capital Grille',
        'address': '444 Brickell Ave, Miami, FL 33131, United States',
        'location': {'lat': 25.769491, 'lng': -80.19032},
        'rating': 4.7,
        'price_level': 4,
        'types': ['bar', 'restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 2160
    },
    {
        'name': 'Il Gabbiano',
        'address': '335 S Biscayne Blvd, Miami, FL 33131, United States',
        'location': {'lat': 25.7716653, 'lng': -80.1852409},
        'rating': 4.4,
        'price_level': 4,
        'types': ['restaurant', 'point_of_interest', 'food', 'establishment'],
        'user_ratings_total': 1333
    },
    {
        'name': "Perricone's Marketplace & Cafe",
        'address': '1700 SW 3rd Ave, Miami, FL 33129, United States',
        'location': {'lat': 25.7611771, 'lng': -80.2001773},
        'rating': 4.4,
        'price_level': 2,
        'types': ['restaurant', 'grocery_or_supermarket', 'point_of_interest', 'food', 'store', 'establishment'],
        'user_ratings_total': 1648
    },
]

console.log(restaurants);

// Get the container div
var container = document.getElementById("restaurants-container");

// Loop through the results and create HTML elements dynamically
restaurants.forEach(function (restaurant) {
    // Create a div for each restaurant
    var restaurantDiv = document.createElement("div");
    restaurantDiv.className = "restaurant";

    // Create HTML content for the restaurant
    var restaurantContent = `
        <h2>${restaurant.name}</h2>
        <p><strong>Address:</strong> ${restaurant.address}</p>
        <p><strong>Rating:</strong> ${restaurant.rating}</p>
        <p><strong>Price Level:</strong> ${generateMoneySigns(restaurant.price_level)}</p>
    `;

    // Set the HTML content to the restaurant div
    restaurantDiv.innerHTML = restaurantContent;

    // Append the restaurant div to the container
    container.appendChild(restaurantDiv);
});


function generateMoneySigns(level) {
    return '$'.repeat(level);
}