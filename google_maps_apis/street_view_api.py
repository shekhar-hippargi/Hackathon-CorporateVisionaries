import googlemaps
from datetime import datetime
from google_streetview import api

def get_google_maps_api_key():
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    return 'AIzaSyDiOm5bW-S9i3eiS1kMEkbPc4dNDQqNnug'

def get_optimized_path(api_key, origin, destination, mode='walking', departure_time='now'):
    gmaps = googlemaps.Client(key=api_key)

    # Get directions for walking
    directions_result = gmaps.directions(
        origin,
        destination,
        mode=mode,
        departure_time=departure_time
    )

    # Extract the polyline from the first route
    polyline_points = directions_result[0]['overview_polyline']['points']

    return polyline_points

def generate_street_view_images(api_key, polyline_points, output_folder):
    # Set up the parameters for the street view request
    params = {
        'location': polyline_points,
        'size': '600x300',  # Specify the image size
        'heading': '0;90;180;270',  # Specify the heading (0, 90, 180, 270 degrees)
        'pitch': '0',  # Specify the pitch (0 degrees)
        'fov': '120',  # Specify the field of view (120 degrees)
    }

    # Make a request to the Street View API and save images to the specified output folder
    results = api.results(params)
    results.download_links(output_folder)

def main():
    api_key = get_google_maps_api_key()
    origin = "1600 Amphitheatre Parkway, Mountain View, CA"  # Google's headquarters
    destination = "1 Infinite Loop, Cupertino, CA"  # Apple's headquarters
    output_folder = "street_view_images"  # Specify the folder to save the images

    polyline_points = get_optimized_path(api_key, origin, destination)

    generate_street_view_images(api_key, polyline_points, output_folder)
    print("Street view images generated.")

if __name__ == "__main__":
    main()
