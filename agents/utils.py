import os
import dill
import uuid
import matplotlib.pyplot as plt
from matplotlib import animation
from path_utils import with_data_root


def read_world_model_from_path(path):
    with open(path, 'rb') as f:
        world_model = dill.load(f)
    return world_model


def save_world_model_to_path(world_model, config=None):
    world_model.clear_cache()
    world_model.clear_precompute_dist()

    unique_id = uuid.uuid4()
    tmp_dir = with_data_root(config, 'tmp_world_models')
    os.makedirs(tmp_dir, exist_ok=True)
    save_path = os.path.join(tmp_dir, f'{unique_id}.pickle')
    with open(save_path, 'wb') as f:
        dill.dump(world_model, f)
    return save_path


def check_overlap(tup1, tup2):
    if tup1[0] > tup2[0]:
        tmp = tup1
        tup1 = tup2
        tup2 = tmp

    return (tup1[1] >= tup2[0])


def save_frames_as_gif(frames, path='./', filename='gym_animation.gif'):
    #Mess with this to change frame size
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0),
               dpi=300)

    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(),
                                   animate,
                                   frames=len(frames),
                                   interval=50)
    anim.save(os.path.join(path, filename),
              writer='imagemagick',
              fps=60 // 3)


def save_frames_as_mp4(frames,
                       frameskip=3,
                       path='./',
                       filename='gym_animation.mp4'):
    # Set up the figure with no padding and lower DPI for better performance
    plt.figure(figsize=(frames[0].shape[1] / 72.0, frames[0].shape[0] / 72.0),
               dpi=60)  # Reduced DPI from 300 to 150
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])
        return [patch]  # Return the patch for blitting

    anim = animation.FuncAnimation(plt.gcf(),
                                   animate,
                                   frames=len(frames),
                                   interval=50,
                                   blit=True)  # Enable blitting for faster rendering
    anim.save(os.path.join(path, filename),
              writer='ffmpeg',
              fps=60 // frameskip,
              codec='libx264',  # Use H.264 codec for better compression
              bitrate=2000)  # Adjust bitrate for better quality/size balance
