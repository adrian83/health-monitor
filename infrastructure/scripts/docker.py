
from scripts.command import execute



def docker_login(username, password, proxy_endpoint):
    print("Login to ECR")
    login_cmd = f"docker login --username {username} --password {password} {proxy_endpoint}"
    execute(login_cmd)



def docker_logout(proxy_endpoint):
    print("Logout from ECR")
    logout_cmd = f"docker logout {proxy_endpoint}"
    execute(logout_cmd)



def upload_images(registry_url: str, image_name: str, tag: str):
    print("Push image {image_name} into ECR")
    ecr_image = f"{registry_url}/{image_name}:{tag}"
    print("Tag image")
    execute(f"docker tag {image_name}:{tag} {ecr_image}")
    print(f"Push image")
    execute(f"docker push {ecr_image}")
    print("Image successfully pushed to ECR")
