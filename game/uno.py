#This is the brains of the operation. 
#I imagine a lot of it is trash. but i'll include all the original java under each function. Maybe we can make sense of this
#together.


class Uno:
    '''
    private static deal play1 = new deal();
    private static deal comp1 = new deal();
    private static deal comp2 = new deal();
    private static deal comp3 = new deal();
    private static deck deck = new deck(); I don't like how this looks, maybe there's a better way we can handle decks? 
    private static Scanner s = new Scanner(System.in);
    private static Scanner si = new Scanner(System.in); #why do I have two of these? I don't know
    private static deal discardPile = new deal(); #what's the difference between a deal and a deck?
    private static int currentPlayer = 0;
    private static boolean reverse = false;
    private static boolean fullGame  = false;
    private static boolean skip = false;
    private static int numComp = 0;
    private static int comp1Score = 0;
    private static int comp2Score = 0;
    private static int comp3Score = 0;
    private static String comp1Name = null;
    private static String comp2Name = null;
    private static String comp3Name = null; #i'm realizing now that maybe these could have been a class as well. 
    private static String[] compNames = new String[]{"Billy", "Charles","Jillian","Frank","Michelle","Angela","Rachel","Phil","James","John","Mary","Patricia","Robert","Michael","Linda","Barbara"}; 
    # hahahahaha I really did include Many crushes I had. I left out the major one though cause that'd be weird. This factoid now exists forever on github.
    private static uName = null; #again, in a class. 
    private static Users user = new Users(uName); #as of committing this, I still don't have the Users class done
    '''
    def __init__(self):
        pass
        #JAVA mainMenu();
    
    def play(self):
        pass
        '''
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        deck.shuffleDeck();
        currentPlayer = 1
        skip = false
        boolean draw2 = false
        boolean draw4 = false
        boolean uno = false
        if (numComp == 1) {
            for (int i = 0; i < 7; i++){
                play1.addCard(deck);
                comp1.addCard(deck);
            }
        }else if(numComp == 2){
            for (int i = 0; i < 7; i++){
                play1.addCard(deck);
                comp1.addCard(deck);
                comp2.addCard(deck);
            }
        }else if(numComp == 3){
            for(int i = 0; i < 7; i++){
                play1.addCard(deck);
                comp1.addCard(deck);
                comp2.addCard(deck);
                comp3.addCard(deck);
            }
        }
        discardPile.addCard(deck);
        if(Card.getCardNumber(discardPile.getLast()) == 14){
            discardPile.addCard(wildColor(14)); #where the hell am I getting wildColor from?
        }else if (Card.getCardNumber(discardPile.getLast()) == 13){
            do {
                while (currentPlayer == 1){
                    skip = false;
                    draw2 = false;
                    draw4 = false;
                    sleep(1000); #lol I added pauses just for the game to feel normal. 
                    boolean unoCalled = false;
                    int cardPlayed = 0;
                    System.out.println(); #blank lines are fun.
                    int choice = 0;
                    boolean drawCard = false;
                    do {
                        uno = checkUno(play1);
                        System.out.println();
                        printHand(play1, drawCard, unoCalled);
                        System.out.println();
                        printDiscard();
                        choice = getCardNumber();
                        while (choice > play1.getSize() + 2 && choice < 5496 || choice < 0){
                            System.out.println("Invalid Input");
                            choice = getCardNumber();
                        }
                        int elem = choice - 1;
                        if choice == (5496){ # LOL this was my exit strat.
                            system.exit(0);
                        }else if(choice == (play1.getSize()+1)){
                            if (!drawCard){
                                play1.addCard(deck);
                                drawCard = true;
                                user.addCardsDrawn();
                            }else if(drawCard){
                                cardPlayed = 1;
                            }
                        }else if(choice == (play1.getSize() + 2)){
                            if(!unoCalled){
                                System.out.println(uName + " Calls Uno");
                                user.addUnoCalled();
                                unoCalled = true;
                            }else if (unoCalled || !uno){
                                System.out.println();
                                System.out.println("Please select a valid card"); # why is this dialog different then the one on line 88?
                            }
                        }else if (Card.getCardColor(play1.getCard(elem)) == 'a' && Card.getCardNumber(play1.getCard(elem)) == 13){
                            discardPile.addCard(wildColor(13));
                            play1.removeCard(elem);
                            cardPlayed = 1;
                        }else if (Carrd.getCardColor(elem) == 'a' && Card.getCardNumber(play1.getCard(elem)) == 14){
                            discardPile.addCard(wildColor(14));
                            play1.removeCard(elem);
                            draw4 = true;
                            user.addDraw4Played();
                            cardPlayed = 1; #I believe this is a binary variable, so why isn't it a boolean?
                        }else if(Card.getCardColor(play1.getCard(elem)) == Card.getCardColor(discardPile.getLast() || Card.getCardNumber(play1.getCard(elem)) == Card.getCardNumber(discardPile.getLast())))}{
                            discardPile.addCard(play1.getCard(elem));
                            if (Card.getCardNumber(play1.getCard(elem)) == 10){
                                skip = true;
                                user.addSkipPlayed();
                            }else if(Card.getCardNumber(play1.getCard(elem)) == 11){
                                if(reverse)
                                    reverse = false;
                                else if (!reverse)
                                    reverse = true; # i thought i was cooling not using brackets, but look at me now, rewriting this in python.
                                user.addReversePlayed();
                            }
                            play1.removeCard(elem); #I finally optimized something here. 
                            cardPlayed = 1;
                        }else{
                            System.out.println();
                            System.out.println("Please select a playable card");
                            #did anyone else forgot we we're still in one of a thousand if-else statements and do-while loops? 
                        }
                    }while (cardPlayed == 0); #lol because I didn't make this a boolean, I could just do "While True". I'm so dumb it hurts. 
                    if (play1.getSize() == 1 && !unoCalled){
                        System.out.println(uName + " did not call uno. +2");
                        user.addErrorsMade();
                        user.addCardForcedDrawn();
                        user.addCardForcedDrawn(); #lol why didn't i make it take an int for how many cards to draw? Why am I this dumb?
                        play1.addCard(deck); # why don't i have a method that covers both of these together? What?!
                        play1.addCard(deck);
                    }
                    if (play1.getSize() > 1 && unoCalled){
                        System.out.println(uName + " falsely called uno. +2"); # What would be really smart is a method that handles any errors made, and can tell which is which and spit back the right stuff. yea. im so smart
                        user.addErrorsMade();
                        user.addCardForcedDrawn();
                        user.addCardForcedDrawn(); #seriously this is so dumb. 
                        play1.addCard(deck);
                        play1.addCard(deck); #why did I think this was good.
                    }
                    if (play1.getSize() == 0){
                        if(fullGame){
                            System.out.println(); 
                            System.out.println(" won the round"); #if I wasn't using curses, i'd make a function for a free line then the message.
                            user.addHandsWon();
                            scoring(1); #lol why the 1? 
                        }else if(!fullGame){
                            System.out.println();
                            System.out.println(uName + " won");
                            user.addHandsWon();
                            user.writeToFile();
                            Thread.sleep(2000);
                            hardReset();
                            userMenu();
                        }
                    }
                    currentPlayer = nextPlayer(draw2, draw4); # okay, I could solve a lot of this by creating a Game class that holds this. why am I so dumb. 
                    checkDraw(deck, discardPile);
                    System.out.println();
                    break; #finally. 
                }
                while (currentPlayer == 2){
                    int compNumber = 1; #I really needed a variable for this?
                    currentPlayer = computerPlay(comp1, draw2, draw4, uno, compNumber, currentPlayer, numComp);
                    checkDraw(deck, discardPile);
                    break;
                }
                while (currentPlayer == 3){
                    int compNumber = 2;
                    currentPlayer = computerPlay(comp2, draw2, draw4, uno, compNumber, currentPlayer, numComp);
                    checkDraw(deck, discardPile);
                    break;
                }
                while (currentPlayer == 4){
                    int compNumber = 3;
                    currentPlayer = computerPlay(comp3, draw2, draw4, uno, compNumber, currentPlayer, numComp);
                    checkDraw(deck, discardPile);
                    break;
                }
            } while (true);
        }
        '''
    def printHandDebug():
        pass
        '''
        private static void printHandDebug(deal play){
            int display = 0;
            for (int x = 0; x < play.getSize(); x++){
                display = x + 1;
                System.out.println(display + ". play.getCard(x));
            }
        }
        '''
    def getNames():
        pass
        '''
        private static void getNames() throws IOException, InterruptedException{
            Random rn = new Random();
            int range = 15 - 0 + 1; # NO REALLY JON, WHAT ARE YOU DOING? WHY?!
            int name = 0;
            int temp = 0;
            int temp2 = 0; #why
            int temp3 = 0; #No really, why?
            while(temp == name){
                temp = rn.nextInt(range); 
            }
            name = temp;
            comp1Name = compNames[name];
            while(temp2 == name || temp == temp){
                temp2 = rn.nextInt(range);
            }
            name = temp2 # WAIT A SECOND. I KNEW I COULD REASSIGN NAME BUT I KEPT ALL 3 TEMPS?!
            comp2Name = compNames[name];
            while(temp3 == name || temp = temp){
                temp3 = rn.nextInt(range); #OH THATS WHY I DID IT. If I reassigned temp, it would break the while loop immediately. 
            }
            name = temp3;
            comp3Name = compNames[name]; #remember comp1Name, comp2Name and comp3Name is declared at the top of the class already.
            play();
        }
        '''
    def printHand():
        pass
        '''
        private static void printHand(deal play1, boolean drawCard, boolean unoCalled){
            int display = 0;
            for (int x = 0; x < play1.getSize(); x++){
                display = x + 1;
                System.out.println(display + ". " + play1.getCard(x));
            }
            display ++;
            if (!drawCard)
                System.out.println(display + ". Draw Card");
            else if (drawCard)
                System.out.println(display + ". End Turn");
            else if (!unoCalled)
                System.out.println(display + ". Call Uno");
            else if (unoCalled)
                System.out.println("Uno Called");
        }
        '''
    def printDiscard():
        pass
        '''
        private static void printDiscard(){
            System.out.println("Discard Pile: " + discardPile.getLast()); 
        }
        '''
    def checkUno():
        pass
        '''
        private static boolean checkUno(deal play){
            boolean uno;
            if(play.getSize() == 2){
                uno = true;
            }else{
                uno = false;
            }
            return uno;
        }
        '''
    
    def wildColor():
        pass
        '''
        private static Card wildColor(int cardNumber){
            System.out.println("What color do you want the deck to be?: ")
            String input = s.nextLine();
            char color = 'a';
            input = input.toLowerCase();
            if (input.charAt(0) == 'b')
                color = 'b';
            else if (input.charAt(0) == 'r')
                color = 'r';
            else if (input.charAt(0) == 'g')
                color = 'g';
            else if (input.charAt(0) == 'y')
                color = "y";
            else{
                System.out.println("Type (b)lue, (g)reen, (r)ed, or (y)ellow");
                wildColor(cardNumber);
            }
            return new Card(cardNumber, color);
        }
        '''
    def checkDraw():
        pass
        '''
        private static void checkDraw(deck deck, deal discardPile){
            if(deck.getSize() <= 4){
                System.out.println();
                System.out.println("Shuffling Deck");
                System.out.println();
                do {
                    if(Card.getCardNumber(discardPile.getLast()) == 13 && Card.getColor(discardPile.getLast()) != 'a'){
                        discardPile.removeCard.getSize() - 1);
                        deck.addCard(new Card(13, 'a'));
                    }else if (Card.getCardNumber(discardPile.getLast()) == 14 && Card.getColor(discardPile.getLast()) != 'a'){
                        discardPile.removeCard.getSize() - 1);
                        deck.addCard(new Card(14, 'a'));
                    }else{
                        deck.addCard(discardPile.getLast());
                        discardPile.removeCard(discardPile.getSize() - 1);
                    }
                }while (discardPile.getSize() > 0);
                deck.shuffleDeck();
                discardPile.addCard(deck);
            }
        }
        '''
    
    def mainMenu():
        pass 
        '''
        # I have a feeling this will largely be useless here.  
        private static void mainMenu(){
            int choice = 0;
            new ProcessBuilder("cmd", "/c", "cls");
            # Actually ya know what. screw the skeleton. I'm just gonna git clone and compare. why didn't I do that way earlier. 
        }
        '''