import tkinter as tk
import tkinter.font as tkFont
import random






###### Constants and setup variables ############
timer_id = "00:00"
wpm = 0
current_count = 0

prompts = [
    "Early in the morning, the city feels like a different place entirely. Streets that are usually packed with noise and motion sit quietly, broken only by the sound of a distant bus or a jogger’s footsteps. Coffee shops begin to glow from the inside, their windows fogged slightly as machines warm up for the day. People move with intention but without urgency, enjoying the rare calm before schedules take over. This brief window of stillness offers a chance to think clearly, to plan, or simply to exist without distraction. As the sun rises higher, the calm slowly dissolves, replaced by the familiar rhythm of traffic, conversations, and notifications. Yet those who notice the morning’s quiet often carry a sense of balance with them long after it fades.",

    "Learning a new skill can feel frustrating at first, especially when progress seems slow. Mistakes appear frequently, and improvement is often difficult to measure day by day. However, small efforts compound over time in ways that are not immediately obvious. Each repetition strengthens understanding, even when it feels unproductive in the moment. Consistency matters more than intensity, and patience becomes a powerful tool. Over weeks and months, the unfamiliar starts to feel natural, and tasks that once required full concentration begin to flow automatically. Looking back, the early struggles become proof of growth rather than failure. Mastery is rarely dramatic; it is quiet, gradual, and built through persistence rather than talent alone.",

    "Rainy afternoons tend to slow everything down, inviting reflection and comfort. The sound of rain against windows creates a steady rhythm that makes it easier to focus or relax. People move more deliberately, choosing warm drinks, soft lighting, and familiar routines. Time feels less demanding, stretching gently instead of rushing forward. Books seem more engaging, music more immersive, and thoughts more organized. Even simple tasks take on a calmer tone. While rain can disrupt plans, it also creates space for rest and creativity. In these moments, productivity doesn’t mean speed; it means presence. A rainy day reminds us that slowing down is sometimes the most efficient way to reset.",

    "Technology has reshaped how people communicate, learn, and work, often in ways that feel invisible. Messages travel instantly across continents, and information is accessible within seconds. While this convenience is powerful, it also demands discipline. Constant alerts compete for attention, fragmenting focus and shortening patience. Choosing when to disconnect becomes just as important as staying informed. Healthy use of technology requires intention rather than habit. When tools are used deliberately, they amplify creativity and efficiency instead of overwhelming them. The challenge lies not in rejecting technology, but in shaping it to support meaningful goals. Balance turns powerful systems into helpful partners instead of constant distractions.",

    "Walking through nature has a unique ability to reset the mind. Trails, trees, and open skies provide a sense of scale that daily routines often lack. Problems that once felt urgent shrink slightly with each step forward. Breathing becomes deeper, thoughts slow down, and awareness sharpens. Even short walks can restore clarity and improve mood. Nature doesn’t demand attention the way screens do; it invites it gently. This quiet engagement encourages reflection without pressure. Over time, regular moments outdoors can improve focus, reduce stress, and inspire creativity. Nature reminds us that stillness and movement can coexist, working together to restore balance.",

    "Creativity rarely appears on command, despite popular belief. More often, it emerges after consistent effort and routine. Showing up regularly creates opportunities for ideas to surface naturally. The process involves experimentation, mistakes, and revision, not sudden inspiration. By allowing imperfect drafts to exist, creativity gains room to grow. Fear of failure often blocks progress more than lack of skill. When judgment is delayed, exploration becomes easier. Over time, patterns form, confidence builds, and originality develops through practice. Creativity is not a moment; it is a habit shaped by patience, curiosity, and willingness to begin without certainty.",

    "Good habits are built quietly, without dramatic milestones or immediate rewards. They rely on repetition rather than motivation, forming through small decisions made consistently. Skipping one day may seem insignificant, but repeating that choice creates momentum in the wrong direction. Structure supports habits when motivation fades. Simple systems reduce friction and make progress easier to sustain. Over time, habits reshape identity, influencing how challenges are approached and goals are pursued. The results may appear gradual, but they are lasting. Success often comes not from bold actions, but from reliable behaviors practiced daily without much attention.",

    "Traveling to unfamiliar places changes perspective in subtle ways. New environments disrupt routines and encourage awareness of details often overlooked at home. Languages, customs, and rhythms of life differ, reminding travelers that no single way of living is universal. Small challenges, like navigating public transportation or ordering food, build confidence and adaptability. Experiences become stories, and memories gain depth through contrast. Even short trips can refresh curiosity and appreciation. Travel does not require distance to be meaningful; it requires openness. Seeing the world through different contexts helps people better understand both others and themselves.",

    "Working through a difficult problem often feels unproductive at first. Progress comes in fragments rather than clear steps forward. Ideas fail, assumptions break, and frustration builds. However, persistence allows patterns to emerge from confusion. Stepping away briefly can provide insight that effort alone cannot. Breaks offer perspective, turning obstacles into manageable parts. Eventually, understanding clicks into place, not because of a single moment, but because of accumulated effort. Solving problems teaches patience and resilience. The struggle itself strengthens skills that apply far beyond the original challenge.",

    "Time management is less about controlling every minute and more about choosing priorities wisely. Schedules provide structure, but flexibility allows adjustment when plans change. Overloading days with tasks reduces focus and increases stress. Intentional planning creates space for both productivity and rest. Knowing when to stop is as important as knowing when to start. Energy levels matter more than hours worked. By aligning tasks with attention and motivation, efficiency improves naturally. Managing time effectively means respecting limits while making progress toward meaningful goals."
]

def start_timer():
    global current_count, timer_id

    # Reset state
    current_count = 0
    time_lbl.config(text="00:00")
    wpm_label.config(text="WPM: --")

    # Clear textbox
    text_box.delete("1.0", tk.END)

    # Start countdown
    countdown(0)


def countdown(count):
    global timer_id, current_count
        # update timer
    time_lbl.config(text = count)
    minutes = count // 60
    seconds = count % 60
    formatted_time = f"{minutes:02d}:{seconds:02d}"
    time_lbl.config(text=formatted_time)

    # timer tick
    timer_id = root.after(1000, countdown, count + 1)
    current_count = count

    # update wpm


    whole_input = text_box.get("1.0", tk.END)
    words = whole_input.split()

    try:
        wpm = (len(words)/current_count) * 60
        wpm_label.config(text = f"WPM: {wpm:.2f}")
    except ZeroDivisionError:
        wpm_label.config(text = f"WPM: --")


def stop_timer():
    global timer_id

    if timer_id is not None:
        root.after_cancel(timer_id)



def prompt_gen():
        # Create the new Toplevel window
        new_window = tk.Toplevel(root)
        new_window.title("Prompt")
        new_window.geometry("300x350")  # Set the window size

        # Add widgets to the new window
        prompt_widget = tk.Text(new_window,wrap=tk.WORD, font=custom_font)
        prompt_widget.pack(padx=5, pady=5)
        prompt_widget.insert(tk.INSERT,random.choice(prompts))
        tk.Button(new_window, text="Close", command=new_window.destroy).pack()

###### Build GUI ###############
root = tk.Tk()
root.geometry("220x300")
root.title("Type Time")
custom_font = tkFont.Font(family="Times New Roman", size=12, weight="bold")


text_box = tk.Text(root, width=20, height=10, padx=10, pady=10)
text_box.grid(column=1,row=0, columnspan=2, padx=20, pady=10)

prompt_gen_btn = tk.Button(root, text="Generate prompt", command=prompt_gen)
start_btn = tk.Button(root, text="Start", command=start_timer)
start_btn.grid(column= 1, row=1)
stop_btn = tk.Button(root, text="Stop", command=stop_timer)
stop_btn.grid(column= 2, row=1 )
# timer = "00:00"
time_lbl = tk.Label(root, text=f"time: {timer_id}")
time_lbl.grid(column=1 , row=2 )
wpm_label = tk.Label(root, text=f"WPM: {wpm:.2f}")
wpm_label.grid(column=2 , row=2 )
gen_prompt = tk.Button(root, text="Generate prompt", command=prompt_gen)
gen_prompt.grid(column=1, row=3, columnspan=2)





root.mainloop()

