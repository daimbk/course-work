using Godot;
using System;
	
public partial class GameManager : Node
{
	// Static reference to the instance
	public static GameManager Instance { get; private set; }
	
	public int Score;
	public AnimatedSprite2D animSprite;
	private Player player;
	
	public Node CurrentScene { get; set; }
	
	public override void _Ready()
	{
		// Set the static reference when the GameManager is ready
		Instance = this;
		
		Viewport root = GetTree().Root;
		CurrentScene = root.GetChild(root.GetChildCount() - 1);
		player = GetNode<Player>("/root/Game/Player");
	}
	
	public override void _Process(double delta)
	{
	}
	
	public void AddScore(int score)
	{
		Score += score;
		GD.Print("Score: " + Score);

		var scorelbl = GetNode<Label>("/root/Game/Labels/score");
		scorelbl.Text = "You collected " +  Score + " coins";
	}
	
	public void GotoScene(string path)
	{
		// defer to avoid stopping leftover code execution of current scene
		CallDeferred(MethodName.DeferredGotoScene, path);
	}
	
	public void DeferredGotoScene(string path)
	{
		// safe to remove the current scene.
		CurrentScene.Free();
		var nextScene = GD.Load<PackedScene>(path);
		CurrentScene = nextScene.Instantiate();
		GetTree().Root.AddChild(CurrentScene);
		GetTree().CurrentScene = CurrentScene;
	}
}
