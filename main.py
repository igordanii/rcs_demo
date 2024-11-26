import gemini as g
import vonage_connection as vc



vc.send_message(g.send_text_prompt("What is RCS?"+
                                   ". Limit replies up to 8000 characters. Use less if possible."),
                                   "5588988128333")


