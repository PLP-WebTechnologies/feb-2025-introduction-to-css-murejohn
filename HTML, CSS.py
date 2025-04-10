HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Styled Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1 id="main-title">Welcome to My Awesome Page</h1>
        <p class="tagline">A place for interesting things.</p>
    </header>

    <div class="container">
        <img src="placeholder.jpg" alt="A placeholder image">
        <section class="content">
            <h2>About This Section</h2>
            <p>This is some sample text within the content section. We're playing around with CSS to make things look spiffy!</p>
            <ul>
                <li class="list-item">Item One</li>
                <li class="list-item">Item Two</li>
                <li>Item Three</li>
            </ul>
        </section>
    </div>

    <footer>
        <p>&copy; 2025 My Awesome Page</p>
    </footer>
</body>
</html>
CSS

/* General body styling for better readability */
body {
    font-family: 'Arial', sans-serif; /* A common and readable font */
    line-height: 1.6; /* Improves text readability */
    color: #333; /* Dark gray for good contrast */
    background-color: #f4f4f4; /* Light gray background */
    margin: 0; /* Reset default body margin */
    padding: 20px; /* Add some padding around the content */
}

/* Styling the header section using the header tag */
header {
    background-color: #5cb85c; /* A nice green color */
    color: white;
    padding: 20px 0;
    text-align: center;
    margin-bottom: 30px; /* Add space below the header */
}

/* Styling the main title using its ID */
#main-title {
    font-size: 2.5em;
    margin-bottom: 10px;
}

/* Styling the tagline using its class */
.tagline {
    font-style: italic;
    color: #ddd; /* Light gray for the tagline */
}

/* Styling the main container using its class */
.container {
    background-color: white;
    padding: 30px;
    border: 1px solid #ccc; /* Light gray border */
    border-radius: 5px; /* Slightly rounded corners */
    margin-bottom: 30px; /* Space below the container */
    display: flex; /* Using flexbox for layout */
    align-items: center; /* Vertically align items in the container */
}

/* Styling the image within the container */
.container img {
    max-width: 300px;
    height: auto;
    margin-right: 20px; /* Space between the image and text */
    border: 2px solid #bbb; /* Gray border around the image */
    padding: 5px;
    border-radius: 3px;
}

/* Styling the content section using its class */
.content {
    flex-grow: 1; /* Allows the content to take up remaining space */
}

/* Styling the list items using their class */
.list-item {
    color: #007bff; /* A blue color for the list items */
    font-weight: bold;
    margin-bottom: 5px;
}

/* Styling the unordered list */
.content ul {
    padding-left: 20px; /* Add some left padding for indentation */
    list-style-type: square; /* Use square bullets */
}

/* Styling the footer */
footer {
    text-align: center;
    padding: 10px 0;
    color: #777;
    font-size: 0.9em;
    border-top: 1px solid #eee; /* Light top border for separation */