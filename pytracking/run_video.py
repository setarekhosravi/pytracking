import os
import sys
import argparse

env_path = os.path.join(os.path.dirname(__file__), '..')
if env_path not in sys.path:
    sys.path.append(env_path)

from pytracking.evaluation import Tracker


def run_video(tracker_name, tracker_param, videofile, optional_box=None, debug=None, save_results=True, gt_path=None, update_rate=None):
    """Run the tracker on your webcam.
    args:
        tracker_name: Name of tracking method.
        tracker_param: Name of parameter file.
        debug: Debug level.
    """
    tracker = Tracker(tracker_name, tracker_param)
    tracker.run_video_generic(videofilepath=videofile, optional_box=optional_box, debug=debug, save_results=save_results, gt_path=gt_path, update_rate=update_rate)

def main():
    parser = argparse.ArgumentParser(description='Run the tracker on your webcam.')
    parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    parser.add_argument('tracker_param', type=str, help='Name of parameter file.')
    parser.add_argument('videofile', type=str, help='path to a video file.')
    parser.add_argument('--optional_box', type=float, default=None, nargs="+", help='optional_box with format x y w h.')
    parser.add_argument('--gt_path', type=str, default=None, help='ground truth directory')
    parser.add_argument('--update_rate', type=int, default=30, help='updating per specified frames from ground truth')
    parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    parser.add_argument('--save_results', dest='save_results', action='store_true', help='Save bounding boxes')
    parser.set_defaults(save_results=True)

    args = parser.parse_args()

    run_video(args.tracker_name, args.tracker_param,args.videofile, args.optional_box, args.debug, args.save_results, args.gt_path, args.update_rate)


if __name__ == '__main__':
    main()
