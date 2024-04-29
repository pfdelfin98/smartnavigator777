<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $postData = file_get_contents('php://input');
    
    $jsonData = json_decode($postData, true);   
    
    if ($jsonData !== null) {
        $latitude = $jsonData['latitude'];
        $longitude = $jsonData['longitude'];
        

        echo 'Coordinates received successfully';
    } else {
        // Respond with an error message if JSON decoding failed
        http_response_code(400); // Bad Request
        echo 'Error: Invalid JSON data';
    }
} else {
    http_response_code(405);
    echo 'Error: Only POST requests are allowed';
}

?>
