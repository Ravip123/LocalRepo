<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple CSS Animation</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #1a1a1a;
            margin: 0;
        }

        .circle {
            width: 150px;
            height: 150px;
            background: linear-gradient(45deg, #ff00cc, #3333ff);
            border-radius: 50%;
            /* The animation magic happens here */
            animation: pulse 3s infinite ease-in-out;
            box-shadow: 0 0 20px rgba(255, 0, 204, 0.5);
        }

        @keyframes pulse {
            0% {
                transform: scale(1);
                filter: hue-rotate(0deg);
            }
            50% {
                transform: scale(1.5); /* Grow larger */
                filter: hue-rotate(180deg); /* Change color */
            }
            100% {
                transform: scale(1);
                filter: hue-rotate(0deg);
            }
        }
    </style>
</head>
<body>
    <div class="circle"></div>
</body>
</html>