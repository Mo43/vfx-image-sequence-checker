from pathlib import Path

def check_sequences(folder):
    filenames = []
    sequences = {}
    
    for file_path in folder.iterdir():
        if file_path.is_file():
            filenames.append(file_path.name)
            
    for file in filenames:
        parts = file.rsplit(".", 2)
        if len(parts) != 3:
            continue
        if not parts[1].isdigit():
            continue
        sequence_name = parts[0]
        frame_number = int(parts[1])
        extension = parts[2].lower()
        
        sequence_key = (sequence_name, extension)
        if sequence_key not in sequences:
            sequences[sequence_key] = []
        sequences[sequence_key].append(frame_number)
        
    incomplete = []
    complete = []
    for (sequence_name,extension),frames in sequences.items():
        smallest=min(frames)
        biggest=max(frames)
        
        found = set(frames)
        missing = []
        for frame in range(smallest,biggest +1):
            if frame not in found:
                missing.append(frame)
                
        if missing:
            incomplete.append(
                f"⚠️ INCOMPLETE: {sequence_name}.{extension}\n"
                f"Missing frames: {', '.join(map(str, missing))}\n")
        else:
            complete.append(
                f"✅ COMPLETE: {sequence_name}.{extension}\n"
                f"No missing frames found\n")
            
    total = len(incomplete) + len(complete)
    if total == 1:
        word = "sequence"
    else:
        word = "sequences"
        
    summary =f"{total} {word} checked, {len(incomplete)} with missing frames"
    
    if not incomplete and not complete:
            return []
    return [summary + "\n"] + incomplete + complete


